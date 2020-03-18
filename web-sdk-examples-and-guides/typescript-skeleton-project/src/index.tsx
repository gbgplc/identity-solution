import * as IDaaS from '../sdk/idaas.gbg';

import { Activities, Activity, ActivityActions, ActivityState, DeepPartial, DocumentAction, IActivityRequest, IAddressToVerify, ISDKState, JourneyActions, PeopleVerifyFieldNames, Provider, Tolerance } from '../sdk/idaas.gbg';


class SDK {

	private sdkInstance: IDaaS.SDK = new IDaaS.SDK();
	public isFieldRequired = (name: string) => {
		return true;
	}

	constructor() {
	}

	public do_configure() {

		return this.sdkInstance.configure({
			baseServiceUrl: 'https://api.gbgplc.com',
			providerConfiguration: {
				[Provider.None]: true
			},
			templates: {
				[IDaaS.Templates.JourneyOverview]: {
					provider: `
						<div key="journey-overview">
							<div key="journey-information" class="journey__overview__container">
								{journey.personId ? <p><Translate translationKey="PERSON__ID" />: {journey.personId}</p> : null}
							</div>
							<div key="buttons" class="button__container">
								<button key="abort" data-idaas-element="journey-overview--abort" onClick={onAbort}>
									<Translate translationKey="JOURNEY__ABORT" />
								</button>
								<button key="log-out" data-idaas-element="journey-overview--log-out" onClick={onLogOut}>
									<Translate translationKey="JOURNEY__LOG__OUT" />
								</button>
							</div>
						</div>
					`,
					type: IDaaS.TemplateType.String
				},
				[IDaaS.Templates.PeopleVerifyFormTextField]: {
					bindings: {
						isFieldRequired: this.isFieldRequired,
					},
					provider: `
						<fieldset key={"people-verify--form-field__" + name} data-idaas-element="people-verify--form-field">
							<label key="field-label" htmlFor={name} data-idaas-element="people-verify--form-field--label">
								<Translate translationKey={"PEOPLE_VERIFY__FIELDS__" + name} />
							</label>
							<input
								key="field-input"
								type={type}
								id={name}
								name={name}
								onChange={onChanged}
								data-idaas-element="people-verify--form-field--input"
								value={value}
							/>
						</fieldset>
					`,
					type: IDaaS.TemplateType.String
				}
			},
		})
			.then(() => this.sdkInstance.authenticate({
				clientId: 'ro.client',
				clientSecret: 'secret',
				grantType: 'id_auth',
				idToken: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IllNRUxIVDBndmIwbXhvU0RvWWZvbWpxZmpZVSJ9.eyJhdWQiOiJkNGZhZDMwMC00MjFlLTQ4ZjctOWRhZS1kNDhhNWIwYzlhYmQiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vZDM4M2NjMDQtM2JiZC00NGIzLTg4ODctMmZiYmVmNzYwMzU4L3YyLjAiLCJpYXQiOjE1ODQ0Nzk0NDAsIm5iZiI6MTU4NDQ3OTQ0MCwiZXhwIjoxNTg0NDgzMzQwLCJhaW8iOiI0Mk5nWURCVU9scS9NT045eWFjNVhJc25tY21vQUFBPSIsImF6cCI6ImQ0ZmFkMzAwLTQyMWUtNDhmNy05ZGFlLWQ0OGE1YjBjOWFiZCIsImF6cGFjciI6IjEiLCJvaWQiOiIwOGRkYjg5MS00M2Q3LTQxNGUtYjNhNi1mZmIyZDE3OWUzZTgiLCJzdWIiOiIwOGRkYjg5MS00M2Q3LTQxNGUtYjNhNi1mZmIyZDE3OWUzZTgiLCJ0aWQiOiJkMzgzY2MwNC0zYmJkLTQ0YjMtODg4Ny0yZmJiZWY3NjAzNTgiLCJ1dGkiOiJ1OGJJYU9TcTJrV1BOcEpIX28wa0FRIiwidmVyIjoiMi4wIn0.Oi1JvPxC5uvIz980IX2JQYDNH9dNBbnyalCxc8AfClWOfVC5fms3EfjlzBsgaeP3GFpvTowNflTSLTziubCX47F8saQSFfv7U9R-Mq0ePBFx07NBrosjaz8kXa5lQZjYkVQpuhKBlfnRIdHUBskZTXwQedenT46gV25KkVbsLxnjLvTbw5QM56NxCYAEIm4BPQWjxV6gpVSR9qHEZZJrF1hXqQHX0RQHizvEdu2dTGpUfdXLP_Sy1VeuGzyAvheV5C7PceLwBEYQdnLjrH4OifaLNjEGTKF_k3h1xeCEuIy6xa8AJGCThPFLUqgZ2XZ53jiYXyErHyfH71wjuQqXYQ'
			}));
	}

	public do_initialise() {
		return this.sdkInstance.initialise(document.getElementById('root') as HTMLElement)
			.then(console.debug);
	}

	public do_peopleverify() {
		return this.sdkInstance.performActivity({
			activity: IDaaS.Activities.PeopleVerify
		})
			.then((obj) => {
				console.log(obj);
			})
			.then(() => console.log("done people verify"))
	}

}

let sdk = new SDK();
sdk.do_configure()
	.then(() => sdk.do_initialise())
	.then(() => sdk.do_peopleverify())
alert('done');
