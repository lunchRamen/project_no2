코로나 시대로 지친 사람들을 위해, 나의 영화취향을 분석해주고, 나와 비슷한 영화취향 사람들과 소통할 수 있게 해주는 사이트입니다.

역할: BE


백엔드파트 설명
- Python Web Framework인 Django를 사용하였습니다.
- config와 apps로 환경설정과 개발코드를 분리했습니다.
- .env로 SECRET_KEY와 다른 외부에 노출되면 안되는 환경변수를 분리해서 관리하였습니다.
- django-restframework(drf)를 이용, Django의 BE적 특성을 살려 RESTful한 통신을 구현했습니다.
- drf의 Serializer를 통해 React와 DB와의 통신을 JSON으로 직렬,비직렬화해서 구현하였습니다..
- 인증의 경우 로그인시 JWT토큰을 발행하여 Default 인증으로 지정, 토큰으로 인증 구현하였습니다.
- 유저의 인터렉션을 예상해 erd를 그려보고, M2M Field를 사용하여 연결테이블을 만들고, 제어해보았습니다.
- drf의 다양한 API View를 상속받아,더 간단하게 구현하려고 노력해보았습니다.


개발파트
- 개발 환경 설정 및 user를 구현하였습니다.
- 환경설정 폴더 config를 따로 빼고, 중요 키 값들은 .env로 보호하여 관리하였습니다.
- drf를 이용, Django의 BE적 특성을 중점적으로 사용하였습니다.
- drf의 serializer를 이용, FE와의 JSON통신을 더 직관적으로 구현하였습니다.
- drf의 다양한 APIView를 이용, 상속받은 코드를 통해 코드의 구현을 간단하게 하였습니다.
- 인증의 경우 JWT토큰을 사용하여 발행 및 보안인증하게끔 구현하였습니다.
