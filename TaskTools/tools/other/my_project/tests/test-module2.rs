// tests/test_module1.rs
use my_project::modules::module1;

#[test]
fn test_greet() {
    let result = module1::greet();
    assert_eq!(result, "Hello from module1!");
}