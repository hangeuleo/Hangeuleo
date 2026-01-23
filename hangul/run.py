import sys
import tokenize
import io
import os

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
    치환된_줄들 = []
    줄들 = 원본.splitlines(keepends=True)
    
    for 줄 in 줄들:
        앞공백 = len(줄) - len(줄.lstrip())
        내용 = 줄.lstrip()
        
        단어들 = []
        i = 0
        while i < len(내용):
            if 내용[i].isspace():
                단어들.append(내용[i])
                i += 1
                continue
            
            j = i
            while j < len(내용) and not 내용[j].isspace():
                j += 1
            단어 = 내용[i:j]
            
            if 단어 in 치환표:
                단어들.append(치환표[단어])
            else:
                단어들.append(단어)
            
            i = j
        
        새줄 = ' ' * 앞공백 + ''.join(단어들)
        치환된_줄들.append(새줄)
    
    치환코드 = ''.join(치환된_줄들)
    
    try:
        토큰들 = list(tokenize.generate_tokens(io.StringIO(치환코드).readline))
        return tokenize.untokenize(토큰들)
    except tokenize.TokenError:
        print("들여쓰기나 괄호가 맞지 않습니다")
        return None
    except Exception as e:
        print("코드 처리 오류:", e)
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
