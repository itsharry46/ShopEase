from common.models import User, Role


def model_get_user_details(username, password):
    try:
        queryset = User.objects.filter(user_username=username, user_password=password, user_status='Y', is_deleted=False,
                                    user_role_id__role_status='Y', user_role_id__is_deleted=False). \
            select_related('user_role_id'). \
            values('user_id', 'user_first_name', 'user_last_name', 'user_role_id', 'user_role_id__role_name')

        queryset = queryset.first()

        return queryset
    
    except Exception as ex:
        print('model_get_user_details exception => ', ex)