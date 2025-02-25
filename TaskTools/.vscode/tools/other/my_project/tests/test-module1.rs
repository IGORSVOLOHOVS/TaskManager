// tests/test_module2.rs
use my_project::modules::module2;

#[test]
fn test_greet() {
    let result = module2::greet();
    assert_eq!(result, "Hello from module2!");
}