# Trains the Prompt Injection Shield and saves model.joblib
import joblib
import matplotlib.pyplot as plt
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

# Public dataset: text + label (1 = attack, 0 = safe)
ds = load_dataset("deepset/prompt-injections")
X_train, y_train = ds["train"]["text"], ds["train"]["label"]
X_test, y_test = ds["test"]["text"], ds["test"]["label"]
print("Train size:", len(X_train), "| Test size:", len(X_test))

model = make_pipeline(
    TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), lowercase=True),
    LogisticRegression(max_iter=2000, C=10, class_weight="balanced"),
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred, target_names=["safe", "attack"]))

ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=["safe", "attack"])
plt.title("Prompt Injection Shield - Confusion Matrix")
plt.savefig("confusion_matrix.png", dpi=150, bbox_inches="tight")

joblib.dump(model, "model.joblib")
print("Saved model.joblib and confusion_matrix.png")
