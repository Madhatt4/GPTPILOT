# main.py
import builtins
import os

import sys
import traceback

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError('Python environment for GPT Pilot is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()

from utils.style import color_red
from utils.custom_print import get_custom_print
from helpers.Project import Project
from utils.arguments import get_arguments
from utils.exit import exit_gpt_pilot
from logger.logger import logger
from database.database import database_exists, create_database, tables_exist, create_tables, get_created_apps_with_steps

from utils.settings import settings, loader
from utils.telemetry import telemetry

def init():
    # Check if the "euclid" database exists, if not, create it
    if not database_exists():
        create_database()

    # Check if the tables exist, if not, create them
    if not tables_exist():
        create_tables()

    arguments = get_arguments()

    logger.info('Starting with args: %s', arguments)

    return arguments


if __name__ == "__main__":
    ask_feedback = True
    project = None
    run_exit_fn = True

    args = init()

    try:
        # sys.argv.append('--ux-test=' + 'continue_development')

        builtins.print, ipc_client_instance = get_custom_print(args)

        if '--api-key' in args:
            os.environ["OPENAI_API_KEY"] = args['--api-key']
        if '--api-endpoint' in args:
            os.environ["OPENAI_ENDPOINT"] = args['--api-endpoint']

        if '--get-created-apps-with-steps' in args:
            if ipc_client_instance is not None:
                print({ 'db_data': get_created_apps_with_steps() }, type='info')
            else:
                print('----------------------------------------------------------------------------------------')
                print('app_id                                step                 dev_step  name')
                print('----------------------------------------------------------------------------------------')
                print('\n'.join(f"{app['id']}: {app['status']:20}      "
                                f"{'' if len(app['development_steps']) == 0 else app['development_steps'][-1]['id']:3}"
                                f"  {app['name']}" for app in get_created_apps_with_steps()))

            run_exit_fn = False
        elif '--ux-test' in args:
            from test.ux_tests import run_test
            run_test(args['--ux-test'], args)
            run_exit_fn = False
        else:
            if settings.telemetry is None:
                telemetry.setup()
                loader.save("telemetry")

            if args.get("app_id"):
                telemetry.set("is_continuation", True)

            # TODO get checkpoint from database and fill the project with it
            project = Project(args, ipc_client_instance=ipc_client_instance)
            project.start()
            project.finish()
            telemetry.set("end_result", "success")
    except Exception:
        print(color_red('---------- GPT PILOT EXITING WITH ERROR ----------'))
        traceback.print_exc()
        print(color_red('--------------------------------------------------'))
        ask_feedback = False
        telemetry.set("end_result", "failure")
    finally:
        if run_exit_fn:
            exit_gpt_pilot(project, ask_feedback)
