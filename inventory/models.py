from common.utils import CustomLogging

from common.models import User, Artifact

# Logger details
logger = CustomLogging.setup_logger(__name__)


def model_get_user_details(username, password):
    try:
        queryset = User.objects.filter(user_username = username, user_password = password, user_status = 'Y', is_deleted = False,
                                    user_role_id__role_status='Y', user_role_id__is_deleted=False). \
            select_related('user_role_id'). \
            values('user_id', 'user_first_name', 'user_last_name', 'user_role_id', 'user_role_id__role_name')

        queryset = queryset.first()

        return queryset
    
    except Exception as ex:
        ex_message = 'model_get_user_details exception => ' + ex
        logger.error(ex_message)


def model_get_user_artifacts(role_id):
    try:
        query_set = Artifact.objects.filter(artifact_role_id = role_id, artifact_module_id__module_status = 'Y'). \
            select_related('artifact_module_id'). \
            values('artifact_module_id__module_id', 'artifact_module_id__module_name', 'artifact_module_id__module_icon', 'artifact_module_id__module_link', 'artifact_create_status', 'artifact_read_status', 'artifact_update_status', 'artifact_delete_status'). \
            order_by('artifact_order_id')
        
        query_set = query_set.all()

        return query_set

    except Exception as ex:
        ex_message = 'model_get_user_artifacts exception => ' + ex
        logger.error(ex_message)