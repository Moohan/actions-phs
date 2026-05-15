import yaml
import pytest
from unittest.mock import patch, mock_open
from .validate_workflow_refs import validate_workflow_references

def test_validate_workflow_references_success():
    """Test successful validation of workflow references."""
    mock_workflow = {
        'jobs': {
            'job1': {'uses': './another_workflow.yml'},
            'job2': {'uses': 'actions/checkout@v2'} # External action, should be ignored
        }
    }
    workflow_content = yaml.dump(mock_workflow)

    with patch('glob.glob', return_value=['.github/workflows/main.yml', '.github/workflows/another_workflow.yml']),          patch('builtins.open', mock_open(read_data=workflow_content)),          patch('os.path.basename', side_effect=lambda x: x.split('/')[-1]):

        # This should not raise any exception
        validate_workflow_references()

def test_validate_workflow_references_no_jobs():
    """Test validation when workflow has no jobs."""
    mock_workflow = {'name': 'Empty Workflow'}
    workflow_content = yaml.dump(mock_workflow)

    with patch('glob.glob', return_value=['.github/workflows/empty.yml']),          patch('builtins.open', mock_open(read_data=workflow_content)),          patch('os.path.basename', side_effect=lambda x: x.split('/')[-1]):

        validate_workflow_references()

def test_validate_workflow_references_failure():
    """Test validation failure when a referenced workflow is missing."""
    mock_workflow = {
        'jobs': {
            'job1': {'uses': './missing_workflow.yml'}
        }
    }
    workflow_content = yaml.dump(mock_workflow)

    with patch('glob.glob', return_value=['.github/workflows/main.yml']),          patch('builtins.open', mock_open(read_data=workflow_content)),          patch('os.path.basename', side_effect=lambda x: x.split('/')[-1]):

        with pytest.raises(ValueError, match="Workflow validation failed."):
            validate_workflow_references()

def test_validate_workflow_references_invalid_yaml():
    """Test validation failure when a workflow file has invalid YAML syntax."""
    with patch('glob.glob', return_value=['.github/workflows/invalid.yml']),          patch('builtins.open', mock_open(read_data="invalid: yaml: :")),          patch('os.path.basename', side_effect=lambda x: x.split('/')[-1]):

        with pytest.raises(ValueError, match="Workflow validation failed."):
            validate_workflow_references()

def test_validate_workflow_references_multiple_errors():
    """Test that multiple errors are reported."""
    mock_workflow = {
        'jobs': {
            'job1': {'uses': './missing1.yml'},
            'job2': {'uses': './missing2.yml'}
        }
    }
    workflow_content = yaml.dump(mock_workflow)

    with patch('glob.glob', return_value=['.github/workflows/main.yml']),          patch('builtins.open', mock_open(read_data=workflow_content)),          patch('os.path.basename', side_effect=lambda x: x.split('/')[-1]),          patch('sys.stdout') as mock_stdout:

        with pytest.raises(ValueError, match="Workflow validation failed."):
            validate_workflow_references()

        # Check if both errors were printed (simplified check)
        output = "".join(call.args[0] for call in mock_stdout.write.call_args_list)
        assert "missing1.yml" in output
        assert "missing2.yml" in output
