# 时间轮：槽位、到期与取消

定时器在长延迟后提前触发、取消后仍被回调：槽位没有取模，插入没有按截止时间归档，tick 只触发当前槽不检查截止时间，取消没有清空所有槽，下一截止时间按插入顺序而不是最小堆，批量定时器只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
sched/__init__.py
sched/timing_wheel.py
tests/test_timing_wheel.py
```

## 当前状态

`sched/timing_wheel.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_timing_wheel.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 槽位按截止时间取模
2. 插入按槽归档
3. tick 检查截止时间
4. 取消清理所有槽
5. 下一截止时间取最小
6. 批量定时器统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `sched/timing_wheel.py`
后 15 条用例应全部通过。
