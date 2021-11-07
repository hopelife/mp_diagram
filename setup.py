from setuptools import setup
import mp_diagram

setup(
    name='mp_diagram',
    version=mp_diagram.__version__,
    description='Moon Package for Diagram(Plotly Dash, Plantuml, Draw.io, Notion, ...)',
    url='https://github.com/hopelife/mp_diagram',
    author='Moon Jung Sam',
    author_email='monblue@snu.ac.kr',
    license='MIT',
    packages=['mp_diagram'],
    # entry_points={'console_scripts': ['mp_diagram = mp_diagram.__main__:main']},
    keywords='diagram',
    # python_requires='>=3.8',  # Python 3.8.6-32 bit
    # install_requires=[ # 패키지 사용을 위해 필요한 추가 설치 패키지
    #     'selenium',
    # ],
    # zip_safe=False
)
