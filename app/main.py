# ==== PATCHES (IMPORTANT) ====
from sklearn.impute import SimpleImputer as _SI

_original_si_transform = _SI.transform

def _patched_si_transform(self, X, **kwargs):
    if not hasattr(self, "_fill_dtype") and hasattr(self, "_fit_dtype"):
        self._fill_dtype = self._fit_dtype
    return _original_si_transform(self, X, **kwargs)

_SI.transform = _patched_si_transform

import sklearn.compose._column_transformer as _ct

class _RemainderColsList(list):
    pass

if not hasattr(_ct, "_RemainderColsList"):
    _ct._RemainderColsList = _RemainderColsList
# =================================

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Insurance Premium Predictor")

app.include_router(router)