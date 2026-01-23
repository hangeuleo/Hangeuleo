import sys, tokenize, io, os, re

치환표 = {
    '만약':'if',
    '아니면_만약':'elif',
    '아니면':'else',
    '반복':'for',
    '동안':'while',
    '출력':'print',
    '입력':'input',
    '함수':'def',
    '반환':'return',
    '참':'True',
    '거짓':'False',
    '없음':'None',
    '그리고':'and',
    '또는':'or',
    '아니다':'not',
    '범위':'range',
    '길이':'len'
}

def 코드_치환(원본):
    원본 = re.sub(r'\s+', ' ', 원본)  # 띄어쓰기 여러 개 → 하나로
    원본 = 원본.replace('\n ', '\n')   # 줄 시작 공백 정리
    try:
        토큰 = []
        g = tokenize.generate_tokens(io.StringIO(원본).readline)
        for t in g:
            if t.type == tokenize.NAME and t.string in 치환표:
                토큰.append(tokenize.TokenInfo(t.type, 치환표[t.string], t.start, t.end, t.line))
            else:
                토큰.append(t)
        return tokenize.untokenize(토큰).decode('utf-8')
    except tokenize.TokenError as e:
        print("들여쓰기 또는 괄호 오류가 있습니다.")
        print(e)
        return None
    except Exception as e:
        print("코드 처리 중 오류:", e)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python run.py 파일명.kor")
        sys.exit(1)
    파일 = sys.argv[1]
    if not os.path.isfile(파일):
        print("파일 없음:", 파일)
        sys.exit(1)
    with open(파일, 'r', encoding='utf-8') as f:
        원본 = f.read()
    치환 = 코드_치환(원본)
    if 치환 is None:
        sys.exit(1)
    exec(치환, globals(), locals())
