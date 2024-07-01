### Установка:

```bash
git clone https://github.com/ipodprugin/auchan-test-task.git && cd auchan-test-task
cp example.env .env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Запуск:

```bash
python3 main.py
```

---

Скрипт записывает в результирующий файл "развёрнутые" диапазоны.  
Если это не требуется, можно решить задачу bash командой:

```bash
tr -d '\"' < {filepath} | tr ',' '\n' | sort -n > {outfile}
```
