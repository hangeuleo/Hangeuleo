import sys
import tokenize
import io
import os

치환표 = {
    '만약': 'if',
    '아니면_만약': 'elif',
    '아니면': 'else',
    '반복': 'for',
    '동안': 'while',
    '출력': 'print',
    '입력': 'input',
    '함수': 'def',
    '반환': 'return',
    '참': 'True',
    '거짓': 'False',
    '없음': 'None',
    '그리고': 'and',
    '또는': 'or',
    '아니다': 'not',
    '범위': 'range',
    '길이': 'len',
}

def 코드_치환(원본):
    try:
        토큰들 = []
        for 토큰 in tokenize.generate_tokens(io.StringIO(원본).readline):
            if 토큰.type == tokenize.NAME and 토큰.string in 치환표:
                토큰들.append((토큰.type, 치환표[토큰.string], 토큰.start, 토큰.end, 토큰.line))
            else:
                토큰들.append(토큰)
        return tokenize.untokenize(토큰들).decode('utf-8')
    except Exception as e:
        print(f"치환 오류: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python -m hangeul.run 파일명.kor")
        sys.exit(1)

    파일 = sys.argv[1]
    if not os.path.isfile(파일):
        print(f"파일 없음: {파일}")
        sys.exit(1)

    with open(파일, 'r', encoding='utf-8') as f:
        원본 = f.read()

    치환된 = 코드_치환(원본)
    if 치환된 is None:
        sys.exit(1)

    print(f"실행: {파일}")
    print("-"*50)
    exec(치환된, globals(), locals())
