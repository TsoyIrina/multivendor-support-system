from django.shortcuts import render, redirect
from django.urls import reverse

from api import get_resource, get_all_resources, create_resource, update_resource


def show_application(request):
    context = {'error': ''}
    res = get_all_resources('employee/get_current')
    if res['is_ok']:
        employee = res['response'].json()
        if res['response'].status_code == 200:
            employee_id = employee['id']
            context['username'] = employee['user']['username']
            res = get_all_resources('work_plan')['response']
            if res.status_code == 200:
                work_plans = [_ for _ in res.json() if _['engineer']['id'] == employee_id]
                if request.method == "POST":
                    date = request.POST.get('date')
                    sup_work_plans = []
                    for work_plan in work_plans:
                        if (work_plan['start_date'] <= date and work_plan['end_date'] >= date) or date == '':
                            sup_work_plans.append(work_plan)
                    context['work_plans'] = sup_work_plans
                    return render(request, 'employee_application.html', context)

                context['work_plans'] = work_plans
        else:
            context['error'] = employee['detail']
    else:
        context['error'] = res['response']

    return render(request, 'employee_application.html', context)


def show_work_plan_detail(request, pk):
    context = {'error': ''}
    res = get_all_resources('employee/get_current')
    if res['is_ok']:
        employee = res['response'].json()
        if res['response'].status_code == 200:
            employee_id = employee['id']
            context['username'] = employee['user']['username']
            res = get_all_resources('work_plan')['response']
            if res.status_code == 200:
                work_plans = [_ for _ in res.json() if _['engineer']['id'] == employee_id]
                context['work_plans'] = work_plans
        else:
            context['error'] = employee['detail']
    else:
        context['error'] = res['response']
    work_plan = get_resource('work_plan', pk)['response'].json()
    context['work_plan'] = work_plan
    if request.method == "POST":
        content = request.POST.get('content')
        data = {
            "content": content,
            "sender_id": employee['user']['id']
        }
        res = create_resource('message', data)
        if res['is_ok'] and res['response'].status_code == 201:
            message = res['response'].json()
            messages = [_['id'] for _ in work_plan['chat_with_employee']['message']]
            messages.append(message['id'])
            data = {
                "messages_id": messages,
            }
            res = update_resource('chat', work_plan['chat_with_employee']['id'], data)
            if res['is_ok']:
                if res['response'].status_code == 200:
                    url_redirect = reverse('employee:work_plan_detail', kwargs={'pk': pk})
                    return redirect(url_redirect)
    return render(request, 'employee_work_plan_detail.html', context)
