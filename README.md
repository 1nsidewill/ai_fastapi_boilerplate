# 🚀 AI FastAPI Boilerplate

AI 융합연구소 팀을 위한 AI FastAPI Boilerplate에 오신 것을 환영합니다! 🎉 이 보일러플레이트는 FastAPI 프로젝트를 효과적으로 시작하고, 혼선을 줄이며, 도구, 버전, 관행을 모두 통일할 수 있도록 만들어졌습니다.

이 보일러플레이트는 인기 있는 FastAPI Best Practices Repository의 베스트 프랙티스를 따릅니다. 자세한 참고가 필요하면 해당 링크를 확인하세요.

## 🤔 왜 이 보일러플레이트인가요?

그동안 우리 팀은 다음과 같은 문제들을 겪었습니다:

- 서로 다른 Python 버전 사용 🤯
- 혼합된 프레임워크와 비표준 설정 😅
- 일관된 의존성 관리를 위한 Poetry의 부재 📦

이 보일러플레이트를 통해 우리는 모두 Python 3.11.10, FastAPI, 그리고 Poetry를 사용하여 통일된 개발 환경을 갖출 수 있습니다.

## 🚀 시작하기

프로젝트를 클론하고 설치하고 실행하는 방법을 따르세요. 아주 쉽습니다, 약속해요! 🤞

### 1. 레포지토리 클론

```bash
git clone https://github.com/1nsidewill/ai_fastapi_boilerplate.git
cd ai_fastapi_boilerplate
```

### 2. Python 버전 확인

Python 3.11.10을 사용하고 있는지 확인하세요:

```bash
python3 --version
```

### 3. Poetry 설치 및 가상 환경 설정

우리는 Poetry를 의존성 관리 도구로 사용합니다. Poetry가 설치되지 않은 경우 아래 명령어로 설치하세요 (이미 설치되어 있다면 이 단계는 건너뛰세요):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Poetry가 가상 환경을 프로젝트 폴더 내부에 생성하도록 설정합니다:

```bash
poetry config virtualenvs.in-project true
```

### 4. 의존성 설치

Poetry를 사용하여 모든 프로젝트 의존성을 설치하세요:

```bash
poetry install
```

### 5. Poetry 쉘 활성화

가상 환경을 활성화하세요:

```bash
poetry shell
```

### 6. 디버그 모드로 실행

프로젝트를 디버그 모드로 실행하려면 F5 키를 누르세요. 필요 시 `.vscode/launch.json`에서 포트를 수정할 수 있습니다.

### 패키지 추가하기

새 패키지를 추가해야 하나요? 아래 명령어를 사용하세요:

```bash
poetry add <package-name>
```

## 📂 프로젝트 구조

프로젝트 구조는 다음과 같습니다:

```
ai_fastapi_boilerplate/
├── .vscode/
├── env/
├── src/
│   ├── auth/
│   ├── crud/
│   ├── middleware/
│   ├── config.py
│   ├── exceptions.py
│   └── main.py
└── templates/
```

## 📌 주요 디렉터리와 파일

- `.vscode/`: VSCode 설정 파일로, 디버깅을 쉽게 하고 일관된 프로젝트 설정을 유지합니다.
- `env/`: 환경별 설정 파일인 `deployment.env`와 `development.env`를 포함합니다. 비밀 키와 설정은 `.env` 파일로 작성하고, `.gitignore`에 등록하세요.
- `src/`: 주요 앱 디렉터리:
  - `auth/` 및 `crud/`: 비즈니스 로직별로 나누어 구조화되어 있습니다.
  - `middleware/`: 세션 관리와 같은 기능을 처리합니다.
  - `config.py`: 로컬 또는 배포 환경에 따라 설정을 읽어옵니다.
  - `exceptions.py`: 애플리케이션에서 사용하는 커스텀 예외를 처리합니다.
  - `main.py`: 앱의 진입점으로, 초기화와 일반 설정을 관리합니다.
- `templates/`: HTML 템플릿들이 저장되는 곳이며, 라우트를 통해 Jinja2로 렌더링됩니다.

## 🛠️ 비즈니스 로직 구성

각 비즈니스 로직 유닛(`auth` 또는 `crud` 등)은 다음을 포함합니다:

- `router.py`: 해당 유닛의 엔드포인트를 정의합니다.
- `schema.py`: Pydantic 모델을 사용하여 엔드포인트에서 사용하는 데이터 구조를 정의합니다.

## 🖼️ HTML 템플릿

- `templates/` 디렉터리에 저장됩니다.
- Jinja2를 사용하여 동적 HTML 콘텐츠를 제공합니다.

## 🎉 이제 시작해볼까요!

이제 준비가 끝났습니다! 이 설정을 통해 의존성을 쉽게 관리하고, 일관된 버전을 유지하며, 코드를 효과적으로 구성할 수 있습니다. 더 자세한 내용이 필요하면 베스트 프랙티스 레포지터리를 참고하거나 저에게 연락하세요!

즐거운 코딩 되세요! 🚀
