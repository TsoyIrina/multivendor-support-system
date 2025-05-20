from django.shortcuts import render, redirect
from django.urls import reverse

from api import get_all_resources, create_resource, update_resource, delete_resource, get_resource


def create_application(request):
    context = {'error': ''}
    res = get_all_resources('company/get_current')
    priority_res = get_all_resources('priority')
    if res['is_ok'] and priority_res['is_ok']:
        if priority_res['response'].status_code == 200:
            company = res['response'].json()
            priority = [_ for _ in priority_res['response'].json() if _['is_active']]
            if res['response'].status_code == 200:
                context = {
                    'username': company['user']['username'],
                    'addresses': company['addresses'],
                    'priority': priority,
                }
                if request.method == 'POST':
                    data = {
                        "company_id": company['id'],
                        "address_id": request.POST.get('address'),
                        "priority_id": request.POST.get('priority'),
                        "lastname": request.POST.get('lastname'),
                        "firstname": request.POST.get('firstname'),
                        "patronymic": request.POST.get('patronymic'),
                        "phone": request.POST.get('phone'),
                        "email": request.POST.get('email'),
                        "serial_number": request.POST.get('serial_number'),
                        "equipment_name": request.POST.get('equipment_name'),
                        "location_in_room": request.POST.get('location_in_room'),
                        "ip_management_interface": request.POST.get('ip_management_interface'),
                        "equipment_non_operational": True if request.POST.get('equipment_non_operational')=='on' else False,
                        "functionality_limited": request.POST.get('functionality_limited'),
                        "suspicion_of_logical_errors": request.POST.get('suspicion_of_logical_errors'),
                        "fault_description":request.POST.get('fault_description')
                    }
                    res = create_resource('application', data)
                    if res['is_ok']:
                        return redirect(reverse('client:application'))
                    else:
                        context['error'] += res['response']
            else:
                context['error'] = company['detail']
    else:
        context['error'] = res['response']

    return render(request, 'create_application.html', context)


def profile(request):
    context = {'error': ''}
    res = get_all_resources('company/get_current')
    if res['is_ok']:
        company = res['response'].json()
        if res['response'].status_code == 200:
            context = {
                'id': company['id'],
                'username': company['user']['username'],
                'name': company['name'],
                'addresses': company['addresses'],
                'date_joined': company['date_joined'],
            }
            if request.method == 'POST':
                data = {
                    'street': request.POST.get('street'),
                    'house_number': request.POST.get('house_number'),
                    'is_active': True
                }
                res = create_resource('address', data)
                if res['is_ok']:
                    address = res['response'].json()
                    if res['response'].status_code == 201:
                        address_id = address['id']
                        addresses_id = [_['id'] for _ in context['addresses']]
                        addresses_id.append(address_id)
                        data = {
                            "user": {
                                "username": context['username'],
                                "is_active": True
                            },
                            "name": context['name'],
                            "addresses_id": addresses_id
                        }
                        update_resource('company', company['id'], data)
                        return redirect(reverse('client:profile'))
                else:
                    context['error'] += res['response']
        else:
            context['error'] = company['detail']
    else:
        context['error'] = res['response']

    return render(request, 'profile.html', context)


def delete_address(request, pk):
    delete_resource('address', pk)
    return redirect(reverse('client:profile'))


def update_profile(request):
    context = {'error': ''}
    res = get_all_resources('company/get_current')
    if res['is_ok']:
        company = res['response'].json()
        if res['response'].status_code == 200:
            context = {
                'id': company['id'],
                'username': company['user']['username'],
                'name': company['name'],
                'addresses': company['addresses'],
                'date_joined': company['date_joined'],
            }
            if request.method == 'POST':
                addresses_id = [_['id'] for _ in context['addresses']]
                data = {
                    "user": {
                        "username": request.POST.get('username'),
                        "is_active": True
                    },
                    "name": request.POST.get('name'),
                    "addresses_id": addresses_id
                }
                update_resource('company', company['id'], data)
                return redirect(reverse('client:profile'))
        else:
            context['error'] = company['detail']
    else:
        context['error'] = res['response']

    return render(request, 'update.html', context)


def show_application(request):
    context = {'error': ''}
    res = get_all_resources('company/get_current')
    if res['is_ok']:
        company = res['response'].json()
        if res['response'].status_code == 200:
            company_id = company['id']
            context['username'] = company['user']['username']
            res = get_all_resources('work_plan')['response']
            if res.status_code == 200:
                work_plans = [_ for _ in res.json() if _['application']['company']['id'] == company_id]
                context['work_plans'] = work_plans
        else:
            context['error'] = company['detail']
    else:
        context['error'] = res['response']

    return render(request, 'application.html', context)


def show_work_plan_detail(request, pk):
    context = {'error': ''}
    res = get_all_resources('company/get_current')
    if res['is_ok']:
        company = res['response'].json()
        if res['response'].status_code == 200:
            company_id = company['id']
            context['username'] = company['user']['username']
            res = get_all_resources('work_plan')['response']
            if res.status_code == 200:
                work_plans = [_ for _ in res.json() if _['application']['company']['id'] == company_id]
                context['work_plans'] = work_plans
        else:
            context['error'] = company['detail']
    else:
        context['error'] = res['response']
    work_plan = get_resource('work_plan', pk)['response'].json()
    context['work_plan'] = work_plan
    if request.method == "POST":
        content = request.POST.get('content')
        data = {
            "content": content,
            "sender_id": company['user']['id']
        }
        res = create_resource('message', data)
        if res['is_ok'] and res['response'].status_code == 201:
            message = res['response'].json()
            messages = [_['id'] for _ in work_plan['chat_with_client']['message']]
            messages.append(message['id'])
            data = {
                "messages_id": messages,
            }
            res = update_resource('chat', work_plan['chat_with_client']['id'], data)
            if res['is_ok']:
                if res['response'].status_code == 200:
                    url_redirect = reverse('client:work_plan_detail', kwargs={'pk': pk})
                    return redirect(url_redirect)
    return render(request, 'work_plan_detail.html', context)


def agreed(request, pk):
    res = get_resource('work_plan', pk)
    if res['is_ok']:
        if res['response'].status_code == 200:
            work_plan = res['response'].json()
            zip_resources_id = [_['id'] for _ in work_plan['zip_resources']]
            data = {
                "application": work_plan['application']['id'],
                "responsible_id": work_plan['responsible']['id'],
                "engineer_id": work_plan['engineer']['id'],
                "status_id": work_plan['status']['id'],
                "zip_resources_id": zip_resources_id,
                "start_date": work_plan['start_date'],
                "end_date": work_plan['end_date'],
                "tasks": work_plan['tasks'],
                "notes": work_plan['notes'],
                "is_agreed": True,
                "chat_with_client": work_plan['chat_with_client']['id'],
                "chat_with_employee": work_plan['chat_with_employee']['id']
            }
            update_resource('work_plan', pk, data)
    url_redirect = reverse('client:work_plan_detail', kwargs={'pk': pk})
    return redirect(url_redirect)
