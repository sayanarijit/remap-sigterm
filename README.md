Run

```bash
poetry install
```

```bash
heroku local
```

In `poetry shell`

```python
import tasks
tasks.add.delay(1, 2)
```
