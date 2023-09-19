def learning_loop(model, data_loader, optimizer, loss_function, num_epochs):
    for epoch in range(num_epochs):
        # Training phase
        model.train()
        total_loss = 0

        for batch in data_loader:
            inputs, targets = batch

            optimizer.zero_grad()

            outputs = model(inputs)
            loss = loss_function(outputs, targets)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        average_loss = total_loss / len(data_loader)

        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {average_loss:.4f}")

        # Evaluation phase (optional)
        if (epoch + 1) % 5 == 0:
            model.eval()
            with torch.no_grad():
                validation_loss = 0

                for batch in validation_data_loader:
                    inputs, targets = batch

                    outputs = model(inputs)
                    loss = loss_function(outputs, targets)

                    validation_loss += loss.item()

                average_validation_loss = validation_loss / len(validation_data_loader)
                print(f"Validation Loss: {average_validation_loss:.4f}")

    print("Training complete!")