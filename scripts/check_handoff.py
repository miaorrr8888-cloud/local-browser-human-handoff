"""Validate task completion evidence after a human browser handoff, offline."""
import argparse,json
from urllib.parse import urlsplit

def check(data):
    if not isinstance(data,dict): raise ValueError('status object required')
    u=urlsplit(data.get('target_url',''))
    if u.scheme!='https' or not u.hostname or u.username or u.password: raise ValueError('target_url must be HTTPS without credentials')
    if not isinstance(data.get('requested_task'),str) or not data['requested_task'].strip():raise ValueError('requested_task required')
    if data.get('original_task_verified') is True:
        evidence=data.get('evidence')
        if data.get('page_visible_after_return') is not True or not isinstance(evidence,dict): raise ValueError('completion needs visible page and evidence object')
        if not all(isinstance(evidence.get(k),str) and evidence[k].strip() for k in ('observed_at','result_url','observed_result')):raise ValueError('completion evidence incomplete')
        state='TASK_REPORTED_COMPLETE'
    elif data.get('page_visible_after_return') is True: state='RESUME_ORIGINAL_TASK'
    else:state='HUMAN_ACTION_REQUIRED'
    return {'state':state,'independently_verified':False,'next_action':{'TASK_REPORTED_COMPLETE':'Review recorded result against requested task','RESUME_ORIGINAL_TASK':'Continue the original business action and capture evidence','HUMAN_ACTION_REQUIRED':'Ask the user to complete verification on the original page'}[state]}

def main():
    p=argparse.ArgumentParser();p.add_argument('status');a=p.parse_args()
    try:r=check(json.load(open(a.status,encoding='utf-8-sig')))
    except (ValueError,TypeError,OSError) as e:p.exit(2,'Input error: '+str(e)+'\n')
    print(json.dumps(r,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
