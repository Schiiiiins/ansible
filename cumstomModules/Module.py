try:
    import json
except ImportError:
    import simplejson as json

from ansible.module_utils.basic import AnsibleModule
import time
import sys

def main():
    module = AnsibleModule(
        argument_spec = dict(
            msg=dict(required=True, type='str')
        )
    )

    msg = module.params['msg']

    try:
        module.exit_json(changed=True, msg='%s - %s' % (time.strftime("%c"), msg))

    except:
        module.fail_json(msg="Error Message")

if __name__ == '__main__':
    main()
