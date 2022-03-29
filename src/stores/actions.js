import { ref, firebaseAuth } from '../config/firebaseConfig';
import axios from 'axios'



// import axios from 'axios'
export const updateCart = ({
  commit
}, {item, quantity, isAdd}) => {
  // TODO: Call service
  commit('UPDATE_CART', {item, quantity, isAdd});
	if (isAdd) {
	//		//${item.title} 
    let message_obj = {
      message: `Sepete eklendi`,
      messageClass: "success",
      autoClose: true
    }
    commit('ADD_MESSAGE', message_obj);
  }
}

export const removeItemInCart = ({commit}, {item}) => {
	commit('REMOVE_CART_ITEM', {item});
}

export const registerByEmail = (_, {email, password}) => {
	return firebaseAuth().createUserWithEmailAndPassword(email, password);
}

export const logout = ({commit}) => {
  commit('SET_CART', []); // clear current cart
  return firebaseAuth().signOut();
}

export function loginWithEmail (_, {email, password}) {
//   return firebaseAuth().signInWithEmailAndPassword(email, password);
	let check = axios.post("http://127.0.0.1:5000/login", { "email": email, "password": password }).then((res) => {
		console.log(res.data["data"])
		return res.data["data"]
	});
	if (check == 0) {
		return null
	}
	else if (check != null) {
		return {"res":check}

	} else {
		return null
	}
}

export function listenToProductList({ commit }) {
  
// 	let products = [ {
//   "description" : "En temelde kağıt grubunda yer alan bir endüstriyel üründür. Özellikle kutu üretiminde ve taşıma sektöründe oldukça pay sahibi olması nedeni ile ön plana çıkar.",
//   "id" : 1,
//   "price" : 180,
//   "quantity" : 100,
//   "thumbnail_url" : "https://n11scdn.akamaized.net/a1/1024/ev-yasam/kartonvekoli/sun-ka-mukavva-70x100-140-mm-30-lu__0951053207730760.jpg",
//   "title" : "MUKAVVA KAĞIT"
// }, {
//   "description" : "Genellikle antetli kağıt, kitap, broşür gibi çalışmaların baskısında kullanılır.Bileşimindeki selüloz miktarı çok, odun miktarı azdır.",
//   "id" : 2,
//   "price" : 150,
//   "quantity" : 15,
//   "thumbnail_url" : "https://www.parafofis.com/image/cache/catalog/products/11027-800x600.webp",
//   "title" : "HAMUR KAĞIT"
// }, {
//   "description" : "Genellikle antetli kağıt, kitap, broşür gibi çalışmaların baskısında kullanılır.Bileşimindeki selüloz miktarı çok, odun miktarı azdır.",
//   "id" : 2,
//   "price" : 150,
//   "quantity" : 15,
//   "thumbnail_url" : "https://www.parafofis.com/image/cache/catalog/products/11027-800x600.webp",
//   "title" : "HAMUR KAĞIT"
// }, {
//   "description" : "Genellikle antetli kağıt, kitap, broşür gibi çalışmaların baskısında kullanılır.Bileşimindeki selüloz miktarı çok, odun miktarı azdır.",
//   "id" : 2,
//   "price" : 150,
//   "quantity" : 15,
//   "thumbnail_url" : "https://www.parafofis.com/image/cache/catalog/products/11027-800x600.webp",
//   "title" : "HAMUR KAĞIT"
// }]
  let products =  axios.get("http://127.0.0.1:5000/products").then((res) => {
    let a = res.data["data"];
	return a
  }).catch((res) => {
	let a = res.data["data"];
	return a
  });
  console.log("AAAAAAAAAA")
  console.log(products)

  
  return commit('UPDATE_PRODUCT_LIST', products);
	
	
}

export function getShoppingCart({ commit }) {
	let cart = []
	// if (uid) {
	// 	return ref.child("cart/" + uid).once('value').then((cart) => {
	// 		// console.log(cart.val());
	// 		if (cart.val() && (!currentCart || currentCart.length == 0)) {
	// 			commit('SET_CART', cart.val());
	// 		}
	// 	});
	// } else {
	// 	// console.log("User has not logged in");
	// }
	return commit('SET_CART', cart);
}

//KUllanıcı giriş yaptıysa shoppingcartı kaydediyor
export function saveShoppingCart(_, {uid, cartItemList}) {
	// console.log("ACTIONS saveShoppingCart");
	// console.log("CART DATA", cartItemList);
	return ref.child("cart/" + uid).set(cartItemList);
}

export function saveToTransaction(_, {uid, cartItemList}) {
	let newTransactionKey = ref.child("transactions").push().key;
	var newTransaction = {}
	newTransaction['/transactions/' + uid + '/' + newTransactionKey] = cartItemList;
	return ref.update(newTransaction);
}
