import setuptools

setuptools.setup(
    name="PyEZFinger",
    version="1.1",
    license='MIT',
    author="seonwoo0808",
    author_email="seonwoo0808@naver.com",
    description="EZ finger recognizing",
    long_description=open('README.md').read(),
    package_data={'': ['finger_model.h5']},
    include_package_data=True,
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)