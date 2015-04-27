FROM dit4c/dit4c-container-ipython

RUN source /opt/python/bin/activate && \
  pip install \
	pandas \
	scikit-learn \
	h5py

RUN mkdir /code
WORKDIR /code
ADD . /code/

