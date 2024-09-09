import logging
"""
logging library 
is a standard python module that allos developers to write log
messages to different output targets. (Console file or external systems)
"""


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("test_logger")

logger.info("Hello, World!")
logger.warning("this will")

"""
1. it provides insights into what is happening within an application.

Why use it ?
1. Debugging: Helps trace issues in the code, especially when trying to understand 
why some code is not working as expected.

2. Monitoring: Helps understand the application's health and performance.

3. Auditing: Records important events or changes that occur in the application.

4. Flexibility: You can log various targets (file, console, email, etc) and 
control the level of detail through log levels(DEBUG, INFO, WARNING, ERROR, CRITICAL).

"""

# Configure logging to a file
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')



# Configure logging to the console
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')


"""
Log Levels
The logging library supports different levels of logging, each representing a different level of severity or detail:

1.DEBUG: Detailed information, typically used for diagnosing problems. 
       It's the lowest level of severity.
2.INFO: General information about the application's progress or state. 
      It's higher than DEBUG.
3.WARNING: Indicates something unexpected happened or might happen in the future. 
         It's used for non-critical issues.
4.ERROR: A serious problem that prevented the application from performing a function.
5.CRITICAL: A very serious error that may prevent the program from continuing to run.
"""



"""
When to use logging ?
1.During Development: Logging can help trace errors, warnings, and code flow without 
  stopping the program like using print() or a debugger would.
2.In Production: Use logging to track the behavior of your application, capture unexpected conditions,
  monitor user interactions, and log important events.
3.Error Handling: Logging errors (with stack traces) helps diagnose issues after the fact, 
  especially in deployed applications.
4.Auditing and Compliance: For tracking operations like database updates, file access, or 
  any other sensitive actions that need to be logged.
"""

"""
Where to use logging in your code?

1.Initialization: Early in your program, set up a logger for your application so you can 
  capture logs throughout its runtime.
2.Inside functions and methods: Log significant operations, especially in areas prone to failure 
  (e.g., file I/O, network calls, database access).
3.Exception Handling: Use logging within try/except blocks to capture detailed error information 
  without terminating the program abruptly.
4.Important Milestones: Log critical checkpoints like when starting or finishing a process or 
when something noteworthy happens.

"""