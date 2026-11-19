"""时间轮：槽位、到期与取消：待实现的核心模块。"""


def slot_for(deadline, tick_ms, slots):
    """截止时间对应槽位。"""
    raise NotImplementedError

def add_timer(wheel, timer_id, deadline, tick_ms, slots):
    """插入定时器。"""
    raise NotImplementedError

def tick(wheel, now, tick_ms, slots):
    """推进并返回到期定时器。"""
    raise NotImplementedError

def cancel(wheel, timer_id):
    """取消定时器。"""
    raise NotImplementedError

def next_deadline(wheel):
    """最近截止时间。"""
    raise NotImplementedError
