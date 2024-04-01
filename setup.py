import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.vNVProtectionOrderNonDV',
      version='0.5.2',
      description=('This petition was developed by CiviLaw.Tech on behalf of Nevada Administrative Office of the Courts as part of their interactive self-help support portal. For more information visit https://www.civilaw.tech'),
      long_description='# Nevada Self-Help Package\r\nA protection order is a court order that requires someone to stay away from you and any locations you identify (such as work, home, etc.).</br>\r\nA "temporary protection order" (a "TPO") may be issued for up to 45 days without notifying the other party first. You must fill out an application, and the judge might want you to come to a hearing if the judge has questions. If approved, the Sheriff will serve the other person with the TPO if you provide a valid local address for them.</br>\r\nYou can also request an "extended protection order." This can be included with your original application, or you can request it later as long as your TPO is in effect. You and the other person will have to go to a hearing where the judge can ask both of you questions before deciding whether to extend the order. The protection order can be extended for up to two years.</br>\r\nThere is no fee to file your application.</br>\r\nYou may want to talk to a domestic violence advocate first about your options. An advocate can help you think about a safety plan so you are prepared before, during, and after a protection order is in place. You can contact the following hotlines to get free information if you are not sure what to do:</br>\r\nSafeNest: 702-646-4981</br>\r\nS.A.F.E. House: 702-564-3227</br>\r\nRape Crisis Center: 702-366-1640\r\n</br>\r\n<hr>\r\nThis interview was developed by CiviLaw.Tech on behalf of Nevada Administrative Office of the Courts as part of their interactive self-help support portal. For more information visit [CiviLaw.Tech](https://www.civilaw.tech).',
      long_description_content_type='text/markdown',
      author='Civilaw.Tech',
      author_email='info@civilaw.tech',
      license='The MIT License (MIT)',
      url='https://www.civilaw.tech',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/vNVProtectionOrderNonDV/', package='docassemble.vNVProtectionOrderNonDV'),
     )

