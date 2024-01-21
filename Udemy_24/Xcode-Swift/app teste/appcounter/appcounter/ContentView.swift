//
//  ContentView.swift
//  appcounter
//
//  Created by MacMini on 17/01/24.
//

import SwiftUI

class Counter: ObservableObject {
    
    @Published var days = 0
    @Published var hours = 0
    @Published var minutes = 0
    @Published var seconds = 0


    init() {
        Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { Timer in
            let calendar = Calendar.current
            let components = calendar.dateComponents([ .day, .hour, .minute, .second], from: Date())
            let currentDate = calendar.date(from: components)
            
            var eventDateComponents = DateComponents()
            eventDateComponents.year = 2024
            eventDateComponents.month = 12
            eventDateComponents.day = 25
            eventDateComponents.hour = 12
            eventDateComponents.minute = 0
            eventDateComponents.second = 0
            
            let eventDate = calendar.date(from: eventDateComponents)
            
            let timeleft = calendar.dateComponents([.day, .hour, .minute, .second], from: currentDate!, to: eventDate!)
            
            self.days = timeleft.day ?? 0
            self.hours = timeleft.hour ?? 0
            self.minutes = timeleft.minute ?? 0
            self.seconds = timeleft.second ?? 0

            
        }
    }
}
struct ContentView: View {
    
    @StateObject var counter = Counter()
    
    var body: some View {
        VStack{
            HStack{
                Text("\(counter.days) dias")
                Text("\(counter.hours) horas")
                Text("\(counter.minutes) minutos")
                Text("\(counter.seconds) segundos")
            }
            
                
        }
       
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
