import sys, tokenize, io, os

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
    lines = 원본.splitlines()
    new_lines = []
    for line in lines:
        stripped = line.lstrip()
        indent = line[:len(line)-len(stripped)]
        words = stripped.split()
        new_words = []
        i = 0
        while i < len(words):
            word = words[i]
            if word in 치환표:
                new_words.append(치환표[word])
            else:
                new_words.append(word)
            i += 1
        new_line = indent + ' '.join(new_words)
        new_lines.append(new_line)
    new_code = '\n'.join(new_lines)
    try:
        토큰 = []
        for t in tokenize.generate_tokens(io.StringIO(new_code).readline):
            토큰.append(t)
        return tokenize.untokenize(토큰).decode('utf-8')
    except:
        print("문법 오류 또는 들여쓰기 확인하세요")
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
