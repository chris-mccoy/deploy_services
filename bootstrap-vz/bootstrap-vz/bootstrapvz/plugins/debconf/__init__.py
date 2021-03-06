def validate_manifest(data, validator, error):
    from bootstrapvz.common.tools import log_check_call, rel_path
    validator(data, rel_path(__file__, 'manifest-schema.yml'))

    # cmm - disable this for now, since we don't have it installed on CentOS
    #log_check_call(['debconf-set-selections', '--checkonly'],
    #               stdin=data['plugins']['debconf'])


def resolve_tasks(taskset, manifest):
    import tasks
    taskset.update([tasks.DebconfSetSelections])
