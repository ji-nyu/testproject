# TestProject API

간단한 유틸리티 API 예제입니다. **의도적으로 문서와 코드가 어긋나 있습니다** (drift detector 데모용).

## API Reference

`add(a: int, b: int) -> int`

두 정수를 더합니다.

`to_upper(text: str) -> str`

문자열을 **대문자**로 변환합니다.



`parse_tags(raw: str) -> list[str]`

쉼표로 구분된 태그 문자열을 파싱하여 **정렬된 고유 태그 목록**을 반환합니다.
`get_users(active: bool = False) -> dict`
활성 사용자 목록을 반환합니다. 반환되는 값은 'users' 키와 'active_only' 키를 포함하는 사전입니다.
