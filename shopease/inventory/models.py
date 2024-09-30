from common.models import User, Role, Artifact, Module, SubModule


def model_get_user_details(username, password):
    try:
        queryset = User.objects.filter(user_username = username, user_password = password, user_status = 'Y', is_deleted = False,
                                    user_role_id__role_status='Y', user_role_id__is_deleted=False). \
            select_related('user_role_id'). \
            values('user_id', 'user_first_name', 'user_last_name', 'user_role_id', 'user_role_id__role_name')

        queryset = queryset.first()

        return queryset
    
    except Exception as ex:
        print('model_get_user_details exception => ', ex)


def model_get_user_artifacts(role_id):
    try:
        query_set = Module.objects.filter(module_status = 'Y', submodule__sub_module_status = 'Y', submodule__artifact__artifact_role_id = role_id). \
            values('module_id', 'module_name', 'submodule__sub_module_id', 'submodule__sub_module_name', 'submodule__sub_module_link', 'submodule__artifact__artifact_create_status', 'submodule__artifact__artifact_read_status', 'submodule__artifact__artifact_update_status', 'submodule__artifact__artifact_delete_status')

        query_set = query_set.all()

        return query_set

    except Exception as ex:
        print('model_get_user_artifacts exception => ', ex)