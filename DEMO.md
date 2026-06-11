# TestProject — Drift Detector 데모

의도적으로 **문서 ↔ 코드 불일치**가 들어 있는 샘플 저장소입니다.

## 포함된 drift 시나리오

| 함수 | 유형 | 문서 | 코드 | 파이프라인 |
|------|------|------|------|------------|
| `get_users` | **Structural** | README `True` / `list[dict]` | `False` / `dict` | 자동 doc patch |
| `get_users` | **Structural** | docstring `list[dict]` | `dict` | patch.diff |
| `to_upper` | **Semantic** | "대문자/uppercase" | `text.lower()` | HITL only (`--detect-semantic`) |
| `parse_tags` | **Semantic** | "정렬된 고유/Sorted unique" | `split` only | HITL only |
| `add` | ✅ 일치 | — | — | drift 없음 |

## 빠른 실행 (기말 폴더에서)

```powershell
cd C:\Users\K\Desktop\기말

# 1) Structural만 (LLM 없음)
python -m docs_code_drift_detector scan testproject -o testproject/output --dry-run-pr

# 2) LLM README + structural patch
$env:OPENAI_API_KEY = "sk-..."
python -m docs_code_drift_detector scan testproject -o testproject/output --use-llm --dry-run-pr

# 3) Semantic HITL 후보 포함
python -m docs_code_drift_detector scan testproject -o testproject/output --use-llm --detect-semantic --dry-run-pr

# 4) GitHub PR (git repo + gh 필요)
python -m docs_code_drift_detector scan testproject -o testproject/output --use-llm --detect-semantic --create-pr --hotl-approved
```

## 기대 결과

### `drift_report.json`

- `get_users` — `return_structure_mismatch`, `parameter_default_mismatch` 등 **structural**
- `to_upper`, `parse_tags` — `semantic_mismatch` (`--detect-semantic` 시)

### `patch.diff`

- `README.md` — `get_users` 시그니처를 코드에 맞게 수정
- `testproject/utils.py` — docstring `Returns` 수정
- **semantic 항목은 patch에 포함되지 않음**

### `pr_dry_run.txt` / GitHub PR 본문

- **Semantic mismatch candidates (HITL)** 섹션에 `to_upper`, `parse_tags`
- **Structural drifts** 섹션에 `get_users` 등

## 로컬 테스트

```powershell
cd testproject
pip install -e ".[dev]"
pytest tests -v
```

테스트는 **코드 동작** 기준이며, 일부러 잘못된 문서와 대비됩니다.

## GitHub 연동

```powershell
cd testproject
git init
git add .
git commit -m "Add intentional drift demo project"
git remote add origin https://github.com/<USER>/testproject.git
git push -u origin main
```

PR 생성은 **testproject가 git 저장소**이고 `gh auth login`이 되어 있어야 합니다.
