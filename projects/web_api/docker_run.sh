docker run -it --rm --shm-size 1g \
    --gpus '"device=5"'  \
    --name mineru-api \
    -p 8765:8765 \
    mineru-api