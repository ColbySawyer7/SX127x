from distutils.core import setup
setup(
  name = 'SX127x',         # How you named your package folder (MyLib)
  packages = ['SX127x'],   # Chose the same as "name"
  version = '0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = '',   # Give a short description about your library
  author = 'Colby Sawyer',                   # Type in your name
  author_email = 'sawyerco21@ecu.edu',      # Type in your E-Mail
  url = 'https://github.com/ColbySawyer7/SX127x.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ColbySawyer7/SX127x/archive/refs/tags/v_0.4.tar.gz',    # I explain this later on
  keywords = ['LoRaWAN', 'Lora', 'Things Network', 'TTN', 'v3'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'RPi.GPIO',
          'spidev',
          'argparse',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)