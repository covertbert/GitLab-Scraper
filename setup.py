from setuptools import setup

setup(name='Gitlab Scraper',
      version='0.1',
      description='Gets stats from Gitlab',
      url='https://github.com/covertbert/GitLab-Scraper',
      author='Bertie Blackman',
      author_email='blackmanrgh@gmail.com',
      license='MIT',
      install_requires=[
          'simplejson', 'python-dotenv'
      ],
      zip_safe=False)
