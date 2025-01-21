#  BRIDGE [Realtime Overlay Translator]

**Realtime Overlay Translator**는 실시간으로 화면에 표시되는 텍스트를 인식하여 번역하고, 번역된 내용을 오버레이로 표시해주는 애플리케이션입니다. 이 도구는 스트리밍 영상, 온라인 강의, 게임 등 다양한 실시간 컨텐츠에서 언어 장벽을 허물어줍니다.

## 주요 기능

- **실시간 텍스트 인식**: Tesseract OCR을 사용하여 화면에 표시되는 텍스트를 실시간으로 인식합니다.
- **즉시 번역**: 인식된 텍스트를 번역 API를 통해 번역합니다.
- **오버레이 표시**: 번역된 텍스트를 화면에 오버레이로 표시하여 사용자가 쉽게 이해할 수 있도록 합니다.

## 데모

![오버레이 예시(발표자료 8번 ppt)](https://github.com/co2plant/Realtime-Overlay-Translator/blob/main/Docs/blob/presentation/008.png)

## 요구 사항

- **Python 3.7 이상**
- **Tesseract OCR**
- **번역 API 키 혹은 번역 모델**
  - Google Translate API 키
  - Naver Papago API 키
  - etc.

## 설치 방법

### 1. 저장소 클론

```PowerShell
git clone https://github.com/co2plant/Realtime-Overlay-Translator.git
cd Realtime-Overlay-Translator
```
### 2. 필요한 Python 패키지 설치
```PowerShell
pip install -r requirements.txt
```
### 3. Tesseract OCR 설치
- Windows:
    [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)에서 설치 파일을 다운로드하여 설치하세요.
- macOS:
    ```PowerShell
    brew install tesseract
    ```
- Linux:
    ```PowerShell
    sudo apt-get install tesseract-ocr
    ```
### 4. 번역 API 키 설정
1. . Naver Papago API 키 발급:
    - [Naver Developers](https://developers.naver.com/docs/papago/)에서 Naver Papago API 키를 발급받으세요.
2. Google Translate API 키 발급:
    - [Google Cloud](https://cloud.google.com/translate/docs/setup?hl=ko#api)에서 Google Translate API 키를 발급받으세요.


## 사용 방법
1. **애플리케이션 실행**:

```PowerShell
python main.py
```

2. **설정:**
   - 올바른 API 키가 설정되어 있는지 확인하세요.
   - OCR 인식 영역 및 오버레이 위치를 설정 파일에서 조정할 수 있습니다.
   - OCR 설치 시 고정 경로로 되어있으므로 C드라이브의 Program Files에 설치되어 있어야합니다.

3. **애플리케이션 사용:**
애플리케이션이 실행되면 실시간으로 화면을 모니터링하여 텍스트를 인식하고 번역된 내용을 오버레이로 표시합니다.