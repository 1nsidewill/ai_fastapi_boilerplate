# 🚀 AI FastAPI Boilerplate

AI 융합연구소 팀을 위한 AI FastAPI Boilerplate에 오신 것을 환영합니다! 🎉 이 보일러플레이트는 FastAPI 프로젝트를 효과적으로 시작하고, 혼선을 줄이며, 도구, 버전, 관행을 모두 통일할 수 있도록 만들어졌습니다.

이 보일러플레이트는 인기 있는 [FastAPI Best Practices Repository](https://github.com/zhanymkanov/fastapi-best-practices)의 베스트 프랙티스를 따릅니다. 자세한 참고가 필요하면 해당 링크를 확인하세요.

## 🤔 왜 이 보일러플레이트인가요?

그동안 우리 팀은 다음과 같은 문제들을 겪었습니다:

- 서로 다른 Python 버전 사용 🤯
- 혼합된 프레임워크와 비표준 설정 😅
- 일관된 의존성 관리를 위한 Poetry의 부재 🛋️

이 보일러플레이트를 통해 우리는 모두 Python 3.11.10, FastAPI, 그리고 Poetry를 사용하여 통일된 개발 환경을 갖출 수 있습니다.

## 🚀 시작하기

프로젝트를 클론하고 설치하고 실행하는 방법을 따르세요. 아주 쉽습니다, 약속해요! 🤞

---

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

Python 3.11.10이 아닌 경우, 다음과 같이 Python 3.11.10을 설치하고 설정하세요:

- **Python 설치**: [Python 다운로드 페이지](https://www.python.org/downloads/release/python-31110/)에서 Python 3.11.10 설치 파일을 다운로드하고 설치합니다.
- **설치 확인**: 설치가 완료되면, 다시 Python 버전을 확인하세요:

```bash
python3 --version
```

- **버전이 올바르게 표시되면**, 다음 단계로 진행합니다. 이미 Python 3.11.10이 설치되어 있다면 이 단계를 건너뛰세요.

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

## 💄 주요 패키지들

이 보일러플레이트에는 다음과 같은 주요 패키지들이 포함되어 있습니다:

- **Python**: 3.11.10 버전을 사용합니다.
- **FastAPI**: `^0.115.5` - 빠르고 효율적인 웹 프레임워크입니다.
- **Uvicorn**: `^0.32.0` - ASGI 서버로 FastAPI를 실행합니다.
- **Pydantic Settings**: `^2.6.1` - 설정 관리 및 환경 변수를 쉽게 처리합니다.
- **Jinja2**: `^3.1.4` - HTML 템플릿 렌더링을 위해 사용됩니다.
- **Itsdangerous**: `^2.2.0` - `session_id`의 서명과 안전한 사용을 보장합니다.

모든 패키지는 [tool.poetry.dependencies] 섹션에 명시되어 있으며, 의존성을 일관되게 관리할 수 있습니다.

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

## 🔧 비즈니스 로직 구성

각 비즈니스 로직 유닛(`auth` 또는 `crud` 등)은 다음을 포함합니다:

- `router.py`: 해당 유닛의 엔드포인트를 정의합니다.
- `schema.py`: Pydantic 모델을 사용하여 엔드포인트에서 사용하는 데이터 구조를 정의합니다.

## 🖼️ HTML 템플릿

- `templates/` 디렉터리에 저장됩니다.
- Jinja2를 사용하여 동적 HTML 콘텐츠를 제공합니다.

## 🛠️ Docker를 사용해 배포하기

AI FastAPI Boilerplate에는 Docker를 사용하여 빠르게 배포할 수 있는 기능도 포함되어 있습니다. 이 가이드는 EC2 인스턴스에서 Docker를 사용하여 FastAPI 앱을 설정하고 실행하는 방법을 설명합니다.

### Step 1: Github에서 프로젝트 클론하기

1. **프로젝트를 클론할 디렉토리로 이동합니다:**

   ```bash
   cd /path/to/your/desired/directory  # 원하는 디렉토리 경로로 조정하세요
   ```

2. **Github에서 저장소를 클론합니다:**

   ```bash
   git clone https://github.com/1nsidewill/ai_fastapi_boilerplate.git
   ```

3. **프로젝트 디렉토리로 이동합니다:**

   ```bash
   cd ai_fastapi_boilerplate
   ```

### Step 2: `.env` 파일 생성

1. **루트 디렉토리 내에 폴더를 생성합니다:**

   ```bash
   mkdir env
   ```

2. **개발용 및 배포용 파일을 생성합니다.** 예시:

   ```bash
   nano env/development.env
   nano env/deployment.env
   ```

3. **각 환경 파일에 환경 변수를 추가합니다.** 예시 (`development.env`):

   ```makefile
   MILVUS_URL=your_milvus_url
   AWS_ACCESS_KEY=your_aws_key
   AWS_SECRET_KEY=your_aws_secret
   UPSTAGE_API_URL=https://api.upstage.ai/v1
   UPSTAGE_API_KEY=your_upstage_api_key
   OPENAI_API_KEY=sk-xxxxx
   ```

4. **파일을 저장하고 종료합니다.** `nano` 사용 시 `CTRL+O`로 저장하고 `Enter`를 눌러 확인 후 `CTRL+X`로 종료할 수 있습니다.

### Step 3: Docker 이미지 빌드

1. **커맨드를 사용하여 Docker 이미지를 빌드합니다:**
   ```bash
   docker build -t ai_fastapi_app .
   ```
   - `-t ai_fastapi_app`: 이미지에 `ai_fastapi_app`라는 이름을 태그로 붙입니다.
   - `.`: 현재 디렉토리를 빌드 컨텍스트로 지정합니다 (`Dockerfile`이 이 디렉토리에 있다고 가정).

### Step 4: Docker 컨테이너 실행

1. **환경 파일과 포트 매핑을 지정하여 컨테이너를 실행합니다:**
   ```bash
   docker run -d --name ai_fastapi_app -p 8000:8000 --env-file env/development.env ai_fastapi_app
   ```
   - `-d`: 백그라운드에서 컨테이너를 실행합니다.
   - `--name ai_fastapi_app`: 컨테이너 이름을 지정하여 관리하기 쉽게 만듭니다.
   - `-p 8000:8000`: 서버의 포트 8000을 컨테이너의 포트 8000에 매핑합니다.
   - DockerFile 내에도 포트 번호를 맵핑하는 라인이 있으니 똑같이 수정해주세요.
   - `--env-file env/development.env`: 개발 환경 변수를 로드합니다. (사실 DockerFile에 # Set environment to deployment ENV ENVIRONMENT=deployment 를 통해 환경을 설정하고, config.py에서 환경에 맞게 변수를 가져오니 필수는 아닙니다)

### Step 5: 설정 확인

1. **컨테이너 상태를 확인하여 정상적으로 실행 중인지 확인합니다:**

   ```bash
   docker ps
   ```

   여기서 `ai_fastapi_app`이 실행 중인 컨테이너 목록에 나타나야 합니다.

2. **로그를 확인하여 오류가 없는지 점검합니다:**

   ```bash
   docker logs ai_fastapi_app
   ```

3. **애플리케이션에 접속합니다:** 브라우저에서 `http://your-ec2-public-ip:8000` (또는 로컬에서 `http://localhost:8000`)에 접속하여 확인합니다.

---

## 🎉 이제 시작해볼까요!

이제 준비가 끝났습니다! 이 설정을 통해 의존성을 쉽게 관리하고, 일관된 버전을 유지하며, 코드를 효과적으로 구성할 수 있습니다. 더 자세한 내용이 필요하면 베스트 프랙티스 레포지터리를 참고하거나 저에게 연락하세요!

즐거운 코딩 되세요! 🚀

