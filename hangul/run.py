import sys
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
    '길이': 'len'
}

def 코드_치환(원본):
    새코드 = 원본
    for 한글, 영어 in 치환표.items():
        새코드 = 새코드.replace(한글, 영어)
    return 새코드

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
    치환된 = 코드_치환(원본)
    exec(치환된, globals(), locals())
