import { firebaseAuth } from '../../config/firebaseConfig';
import {isLogged} from "../../components/auth/Login.vue"
const state = {
	isLoggedIn: isLogged,
	user: firebaseAuth().currentUser,
}

const mutations = {
	'AUTH_STATUS_CHANGE' (state) {
		state.isLoggedIn = isLogged;
		state.user = firebaseAuth().currentUser;
	}
}

const actions = {

}

const getters = {
	isLoggedIn: (state) => {
		return state.isLoggedIn;
	},
	currentUser: (state) => {
		if (state && state.user) {
			return {
				email: state.user.email,
				emailVerified: state.user.emailVerified,
				uid: state.user.uid
			}
		} else {
			return {};
		}
	}
}

export default {
	state,
	mutations,
	actions,
	getters
}
