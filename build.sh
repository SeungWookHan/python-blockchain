docker build -t python-web3 . && docker run          \
--rm                \
-it                 \
-v $(pwd):/app  \
-w /app             \
python-web3 \
/bin/bash