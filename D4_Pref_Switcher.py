import os
from re import findall,search,MULTILINE
from sys import exit

def read_need_fix_setting_to_dict(txt_src):
    with open(txt_src,'r',encoding='utf-8') as f:
        txt_content=f.read()
    tmp_ls = findall('([A-Za-z0-9]+) "([0-9\.]*)"',txt_content,MULTILINE)
    return tmp_ls

def main():
    user_profile = os.environ['USERPROFILE']
    d4_setting_dir = user_profile + "\\Documents\\Diablo IV\\"
    # 先檢測 我的文件\\Diablo IV\\LocalPrefs.txt' 是否存在，若無表示還未曾開啟過 Diablo IV ，彈出訊息提示並結束程式
    if os.path.isfile(f'{d4_setting_dir}LocalPrefs.txt') != True:
        input(f'LocalPrefs.txt 不存在，\n請先執行一次Diablo IV 進到遊戲登入選單後結束遊戲，再重新執行本程式...\n按 [Enter] 離開')
        exit(0)
    # print(d4_setting_dir)
    while 1:
        os.system("cls")
        sel = input(f"Diablo IV LocalPrefs.txt 修改程式 -- 功能選項: \n\n1. 設為視窗模式特效全關.\n2. 回復預設值.\n0. 離開.\n\n請輸入要執行的項目( 0 或 1 或 2 ) : ")
        if sel.strip()=='1' and  os.path.isfile(f'{d4_setting_dir}LocalPrefs.txt'):
            setting_ls= read_need_fix_setting_to_dict('need_fix_setting.txt')
            with open(f'{d4_setting_dir}LocalPrefs.txt','r') as f:
                old_content = f.read()
            #print(old_content)
            for i in setting_ls:
                match = search( f'{i[0]} "[0-9\.]*"',old_content)
                gap1,gap2 = match.span(0)[0],match.span(0)[1]
                #print(gap1,gap2)
                old_content = old_content[:gap1]+f'{i[0]} "{i[1]}"'+old_content[gap2:]
                #print(old_content)
            with open(f'{d4_setting_dir}LocalPrefs.txt','w+') as f:
                f.write(old_content)
            input(f'LocalPrefs.txt 已設為 視窗模式-最低畫質-特效全關，\n可以重新執行Diablo IV 了 ...\n按 [Enter] 離開')
            exit(0)
        elif sel.strip()=='2' and  os.path.isfile(f'{d4_setting_dir}LocalPrefs.txt'):
            os.remove(f'{d4_setting_dir}LocalPrefs.txt')
            input(f'LocalPrefs.txt 已移除，\n請執行Diablo IV 進到遊戲登入選單會自動生成預設的 LocalPrefs.txt ...\n按 [Enter] 離開')
            exit(0)
        elif sel.strip()=='0':
            exit(0)

if __name__ == '__main__': main()