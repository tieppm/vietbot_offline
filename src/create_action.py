import json

act = {}
act['on'] = []
act['on'].append({
    'value': 'bật'
})
act['off'] = []
act['off'].append({
    'value': 'tắt'
})
act['up'] = []
act['up'].append({
    'value': 'lên'
})
act['down'] = []
act['down'].append({
    'value': 'lên'
})
act['open'] = []
act['open'].append({
    'value': 'mở'
})
act['close'] = []
act['close'].append({
    'value': 'đóng'
})
act['connect'] = []
act['connect'].append({
    'value': 'kết nối'
})
act['adjust'] = []
act['adjust'].append({
    'value': 'điều chỉnh'
})
act['disconnect'] = []
act['disconnect'].append({
    'value': 'ngắt'
})
act['check'] = []
act['check'].append({
    'value': 'kiểm tra'
})
act['display'] = []
act['display'].append({
    'value': 'hiển thị'
})
act['enable'] = []
act['enable'].append({
    'value': 'kích hoạt'
})
act['execute'] = []
act['execute'].append({
    'value': 'thực hiện'
})
act['execute'].append({
    'value': 'thực thi'
})
act['execute'].append({
    'value': 'thi hành'
})
act['disable'] = []
act['disable'].append({
    'value': 'vô hiệu'
})
act['cancel'] = []
act['cancel'].append({
    'value': 'hủy bỏ'
})
act['read'] = []
act['read'].append({
    'value': 'đọc'
})
act['tell'] = []
act['tell'].append({
    'value': 'kể'
})
act['listen'] = []
act['listen'].append({
    'value': 'nghe'
})
act['incrase'] = []
act['incrase'].append({
    'value': 'tăng'
})
act['decrase'] = []
act['decrase'].append({
    'value': 'giảm'
})
act['bigger'] = []
act['bigger'].append({
    'value': 'to'
})
act['smaller'] = []
act['bigger'].append({
    'value': 'bé'
})
act['pause'] = []
act['pause'].append({
    'value': 'pause'
})
act['continue'] = []
act['continue'].append({
    'value': 'tiếp tục'
})
act['reply'] = []
act['reply'].append({
    'value': 'phát lại'
})
act['reply'].append({
    'value': 'bật lại'
})
act['next'] = []
act['next'].append({
    'value': 'kế tiếp'
})
act['next'].append({
    'value': 'tiếp theo'
})
act['stop'] = []
act['stop'].append({
    'value': 'stop'
})
act['stop'].append({
    'value': 'dừng'
})
act['stop'].append({
    'value': 'ngừng'
})
act['play'] = []
act['play'].append({
    'value': 'phát'
})
act['play'].append({
    'value': 'chơi'
})
act['sing'] = []
act['sing'].append({
    'value': 'hát'
})
act['download'] = []
act['sing'].append({
    'value': 'tải'
})
act['download'].append({
    'value': 'download'
})
act['setup'] = []
act['setup'].append({
    'value': 'cài'
})
act['setup'].append({
    'value': 'đặt'
})

act['setup'].append({
    'value': 'thiết lập'
})

act['change'] = []
act['change'].append({
    'value': 'thay đổi'
})
act['change'].append({
    'value': 'chỉnh'
})
act['send'] = []
act['send'].append({
    'value': 'gửi'
})
act['send'].append({
    'value': 'chuyển'
})
act['notice'] = []
act['notice'].append({
    'value': 'nhắc'
})
act['schedule'] = []
act['schedule'].append({
    'value': 'lập lịch'
})
act['schedule'].append({
    'value': 'đặt lịch'
})
with open('action.json', 'w') as outfile:
    json.dump(act, outfile)
