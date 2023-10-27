# HolaOdoo
Create my first module

## Create virtual environment
```
virtualenv -p python3.11 venv
```
```
source venv/bin/activate
```
```
pip install -U pip
pip install --upgrade wheel
pip install --upgrade setuptools
```
```
pip install -r requirements.txt
```
```
pip install -e ./
```
```
odoo --version
```
```
odoo -d odoo17 -r odoo17 -w o --without-demo=all --stop-after-init
```
```
odoo -c odoo.conf --save --stop
```
- Edit odoo.conf
```
odoo -c odoo.conf
```
## Create Module
```
odoo scaffold tax_authority ./custom_addons
```
## Install Module
```
odoo -c odoo.conf -i tax_authority
```
## Create folder to icon
```
mkdir -p ./static/description
```
