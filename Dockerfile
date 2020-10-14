FROM    python:3.8.1-slim
WORKDIR /app
COPY    main.py          .
COPY    requirements.txt .
COPY    keys.json        .
RUN     python -m pip install --upgrade pip
RUN     python -m pip install -r requirements.txt
CMD     [ "python", "main.py" ]