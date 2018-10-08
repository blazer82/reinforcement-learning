FROM eboraas/openai-gym

RUN pip install --upgrade pip
RUN pip install --upgrade tensorflow

EXPOSE 8888 6006