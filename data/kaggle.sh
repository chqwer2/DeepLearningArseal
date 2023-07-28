

# Upload

# 1.
kaggle datasets init -p .

# 2.
vim dataset-metadata.json

# 3.
kaggle datasets create -p .

# Update
kaggle datasets version -p . -m "Your message here"

# Download
kaggle datasets download -d calvchen/bilateral

