import React from 'react'
import { connect } from 'react-redux'
import { Checkbox, Radio, FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap'
import styles from '../../css/main.css'


class CurrentEvent extends React.Component {

    constructor(props) {
	super(props);
	this.handleSelect = this.handleSelect.bind(this);
    }

    componentDidMount() {
	const { dispatch } = this.props;
	var dartboard = new Dartboard('#dartboard');
	dartboard.render();
	
    }

    handleSelect(d) {
	const { dispatch } = this.props;
    }

    render() {
	
	return (
	    <div>
		<div id="dartboard" className={styles.dartboard} onClick={this.handleSelect}></div>
	    </div>
	)
    }
}

function mapStateToProps(state, ownProps) {
    return {}
}

export default connect(mapStateToProps)(CurrentEvent)




/* <form>
 * <FormGroup type="text" placeholder="Enter text" value="hehe">
 * <ControlLabel>label</ControlLabel>
 * </FormGroup>
 * <Checkbox checked readOnly>
 * Checkbox
 * </Checkbox>
 * <Radio checked readOnly>
 * Radio
 * </Radio>
 * 
 * <FormGroup>
 * <Checkbox inline>
 * 1
 * </Checkbox>
 * {' '}
 * <Checkbox inline>
 * 2
 * </Checkbox>
 * {' '}
 * <Checkbox inline>
 * 3
 * </Checkbox>
 * </FormGroup>
 * <FormGroup>
 * <Radio name="radioGroup" inline>
 * 1
 * </Radio>
 * {' '}
 * <Radio name="radioGroup" inline>
 * 2
 * </Radio>
 * {' '}
 * <Radio name="radioGroup" inline>
 * 3
 * </Radio>
 * </FormGroup>
 * 
 * <FormGroup controlId="formControlsSelect">
 * <ControlLabel>Select</ControlLabel>
 * <FormControl componentClass="select" placeholder="select">
 * <option value="select">select</option>
 * <option value="other">...</option>
 * </FormControl>
 * </FormGroup>
 * <FormGroup controlId="formControlsSelectMultiple">
 * <ControlLabel>Multiple select</ControlLabel>
 * <FormControl componentClass="select" multiple>
 * <option value="select">select (multiple)</option>
 * <option value="other">...</option>
 * </FormControl>
 * </FormGroup>
 * 
 * <FormGroup controlId="formControlsTextarea">
 * <ControlLabel>Textarea</ControlLabel>
 * <FormControl componentClass="textarea" placeholder="textarea" />
 * </FormGroup>
 * 
 * <FormGroup>
 * <ControlLabel>Static text</ControlLabel>
 * <FormControl.Static>
 * email@example.com
 * </FormControl.Static>
 * </FormGroup>
 * 
 * <Button type="submit">
 * Submit
 * </Button>
 * </form>*/
