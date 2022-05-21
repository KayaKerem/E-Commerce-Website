import Store from './components/Store.vue';
import ShoppingCart from './components/ShoppingCart.vue';
import ProductDetails from './components/ProductDetails.vue';
import Login from './components/auth/Login.vue';
import Register from './components/auth/Register.vue';
import Profile from './components/Profile.vue'
import Main from './components/Main.vue'
import Order from './components/Order.vue';
import OrderDetails from './components/OrderDetails.vue'
import Success from './components/Success.vue';
import Sorry from './components/Sorry.vue'
import Forget from './components/Forget.vue'
export const routes = [
	{path: '/', component: Main, name: 'home'},
	{path: '/product/:id', component: ProductDetails, name: 'product'},
	{path: '/cart', component: ShoppingCart, name: 'shoppingcart'},
	{path: '/login', component: Login, name: 'login', onlyGuest: true },
	{ path: '/register', component: Register, name: 'register', onlyGuest: true },
	{ path: '/store', component: Store, name: 'store', onlyGuest: true },
	{ path: '/profile', component: Profile, name: 'profile', onlyGuest: true },
	{ path: '/order', component: Order, name: 'order', onlyGuest: true },
	{ path: '/orderdetails', component: OrderDetails, name: 'orderdetails', onlyGuest: true },
	{ path: '/success', component: Success, name: 'success', onlyGuest: true },
	{path:'/sorry',component:Sorry,name:'sorry',onlyGuest:true},
	{path:'/forget',component:Forget,name:'forget',onlyGuest:true},
	{ path: '*', redirect: '/' }
];