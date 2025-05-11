from django.contrib.auth import get_user_model

User = get_user_model()

def create_custom_user(strategy, details, backend, user=None, *args, **kwargs):
    print("==== NAVER DETAILS ====")
    print("details:", details)
    print("kwargs:", kwargs)

    if user:
        return {'user': user}

    email = details.get('email')
    nickname = details.get('nickname') or details.get('name') or '네이버사용자'

    user_id = kwargs.get('uid') or email or strategy.session_get('user_id_fallback')

    if not user_id:
        raise ValueError('User ID(이메일일)가 필요합니다.')

    user = User.objects.create_user(
        user_id=user_id,
        email=email or '',
        nickname=nickname,
    )

    return {'user': user}
