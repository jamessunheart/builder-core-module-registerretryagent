import time

class RegisterRetryAgent:
    def __init__(self, pipeline_guardian, max_retries: int = 10, delay: int = 60):
        self.pipeline_guardian = pipeline_guardian
        self.max_retries = max_retries
        self.delay = delay

    def try_register(self, module_name: str, description: str):
        for attempt in range(1, self.max_retries + 1):
            try:
                print(f"Attempt {attempt}: Trying to register {module_name}...")
                # Simulate call to register_module
                raise Exception("Tool 'register_module' not found")  # Placeholder
            except Exception as e:
                self.pipeline_guardian.handle_error(
                    module_name,
                    "register_module",
                    f"Attempt {attempt} failed: {str(e)}"
                )
                time.sleep(self.delay)
        print(f"Failed to register {module_name} after {self.max_retries} attempts.")