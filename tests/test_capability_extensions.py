from pathlib import Path
import importlib.util,unittest,tempfile,json,sys,subprocess,os
ROOT=Path(__file__).resolve().parents[1]
def load(path):
    sys.path.insert(0,str(ROOT/'scripts'))
    spec=importlib.util.spec_from_file_location('extension',ROOT/path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

class Handoff(unittest.TestCase):
    def data(self):return {'target_url':'https://example.com/task','requested_task':'Save draft','page_visible_after_return':True}
    def test_login_only_resumes_task(self):self.assertEqual(load('scripts/check_handoff.py').check(self.data())['state'],'RESUME_ORIGINAL_TASK')
    def test_empty_completion_refused(self):
        data=self.data();data['original_task_verified']=True
        with self.assertRaises(ValueError):load('scripts/check_handoff.py').check(data)
    def test_recorded_completion_is_not_independent(self):
        data=self.data();data.update(original_task_verified=True,evidence={'observed_at':'2026-10-15T00:00:00Z','result_url':'https://example.com/draft/1','observed_result':'Draft saved'})
        self.assertFalse(load('scripts/check_handoff.py').check(data)['independently_verified'])
